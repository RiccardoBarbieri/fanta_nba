import org.jetbrains.kotlin.gradle.tasks.KotlinCompile
import com.bmuschko.gradle.docker.tasks.image.DockerBuildImage
import com.bmuschko.gradle.docker.tasks.image.DockerPushImage
import com.bmuschko.gradle.docker.tasks.image.Dockerfile
import java.util.*

plugins {
    id("org.springframework.boot") version "3.3.0"
    id("io.spring.dependency-management") version "1.1.3"
    id("com.bmuschko.docker-spring-boot-application") version "9.4.0"
    id("application")
    kotlin("jvm") version "1.9.20" // Adjust Kotlin version as needed
}

group = "betapi.swagger"
version = "1.0.0"
description = "bet_api"
java.sourceCompatibility = JavaVersion.VERSION_17

repositories {
    mavenCentral()
}

dependencies {
    implementation("org.springframework.boot:spring-boot-starter-web")
    implementation("org.springframework.boot:spring-boot-starter-tomcat")
    implementation("org.springdoc:springdoc-openapi-ui:1.7.0")
    implementation("com.github.joschi.jackson:jackson-datatype-threetenbp:2.15.2")
    implementation("jakarta.validation:jakarta.validation-api")
    implementation("org.springframework.plugin:spring-plugin-core:3.0.0")
    testImplementation("org.springframework.boot:spring-boot-starter-test")
    implementation("org.jsoup:jsoup:1.17.2")
    implementation("org.springframework.boot:spring-boot-starter-data-mongodb")
    implementation("org.springframework.boot:spring-boot-starter-webflux")
    implementation("org.apache.httpcomponents.client5:httpclient5:5.3.1")
    implementation("org.springframework:spring-web")
}

tasks.withType<KotlinCompile> {
    kotlinOptions {
        jvmTarget = "17"
    }
}

val springProps = Properties()
//properties["activeProfile"]?.let {
//    println("Loading properties from application-$it.properties")
//    springProps.load(file("src/main/resources/application-$it.properties").inputStream())
//}
springProps.load(file("src/main/resources/application.properties").inputStream())

var registryUrl = ""
var registryUsername = ""
var registryPassword = ""

fun loadRegistryInfo(file: File) {
    if (!file.exists()) {
        registryUrl = System.getenv()["ACR_SERVER"] ?: throw GradleException("ACR_SERVER environment variable not set")
        registryUsername = System.getenv()["ACR_USERNAME"] ?: throw GradleException("ACR_USERNAME environment variable not set")
        registryPassword = System.getenv()["ACR_PASSWORD"] ?: throw GradleException("ACR_PASSWORD environment variable not set")
    }
    else {
        val json = groovy.json.JsonSlurper().parseText(file.readText()) as Map<String, String>
        registryUrl = json["server"].toString()
        registryUsername = json["username"].toString()
        registryPassword = json["password"].toString()
    }
}

loadRegistryInfo(file("registry.json"))

tasks.register<Dockerfile>("createDockerfile") {
    mustRunAfter("bootDistTar")
    dependsOn("bootDistTar")
    group = "fantanbadocker"
    description = "Create Dockerfile"

    doFirst {
        val inputTarFile =
            project.layout.projectDirectory.file("build/distributions/" + project.name + "-boot-" + project.version + ".tar")

        if (!inputTarFile.asFile.exists()) {
            throw GradleException("Distribution tar file not found: ${inputTarFile.asFile}, check distributions folder")
        }

        from("openjdk:17")
        exposePort(springProps["server.port"].toString().toInt())
        addFile("./build/distributions/${inputTarFile.asFile.name}", "/")
        workingDir(inputTarFile.asFile.name.removeSuffix(".tar") + "/bin")
        defaultCommand("./" + project.name)
    }
}

tasks.register<DockerBuildImage>("buildImage") {
    dependsOn("createDockerfile")
    group = "fantanbadocker"
    description = "Build the image from the Dockerfile created"
    val dockerRepository = properties["dockerRepository"] ?: throw GradleException("dockerRepository property not set")
    dockerFile.set(file(layout.projectDirectory.toString() + "/build/docker/Dockerfile"))
    inputDir.set(file(layout.projectDirectory))
    images.add("${dockerRepository}/" + project.name + ":latest")
    images.add("${dockerRepository}/" + project.name + ":${project.version}")
}

tasks.register<DockerPushImage>("pushImage") {
    dependsOn("buildImage")
    group = "fantanbadocker"
    description = "Push the docker image to the repository"

    docker {

        registryCredentials {
            url.set(registryUrl)
            username.set(registryUsername)
            password.set(registryPassword)
        }
    }

    val dockerRepository = properties["dockerRepository"] ?: throw GradleException("dockerRepository property not set")
    images.add("${dockerRepository}/" + project.name + ":latest")
    images.add("${dockerRepository}/" + project.name + ":${project.version}")
}

tasks.withType<JavaCompile>() {
    options.encoding = "UTF-8"
}

tasks.withType<Javadoc>() {
    options.encoding = "UTF-8"
}