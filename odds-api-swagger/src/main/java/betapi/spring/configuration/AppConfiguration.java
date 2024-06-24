package betapi.spring.configuration;


import org.springframework.context.annotation.Configuration;
import org.springframework.data.mongodb.repository.config.EnableMongoRepositories;
import org.springframework.scheduling.annotation.EnableScheduling;

@Configuration
@EnableScheduling
@EnableMongoRepositories(basePackages = "com.betapi.database.repositories")
public class AppConfiguration {
}
