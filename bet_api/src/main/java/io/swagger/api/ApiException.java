package io.swagger.api;

@jakarta.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2024-06-24T10:03:13.459259793Z[GMT]")
public class ApiException extends Exception {
    private final int code;
    public ApiException (int code, String msg) {
        super(msg);
        this.code = code;
    }
}
