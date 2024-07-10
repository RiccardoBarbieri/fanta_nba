package betapi.swagger.api;

@jakarta.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2024-06-24T10:03:13.459259793Z[GMT]")
public class NotFoundException extends ApiException {
    private final int code;
    public NotFoundException (int code, String msg) {
        super(code, msg);
        this.code = code;
    }
}
