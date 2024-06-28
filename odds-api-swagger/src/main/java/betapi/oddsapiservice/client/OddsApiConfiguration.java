package betapi.oddsapiservice.client;

import betapi.oddsapiservice.OddsApiService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestClient;
import org.springframework.web.client.support.RestClientAdapter;
import org.springframework.web.service.invoker.HttpServiceProxyFactory;

@Component
public class OddsApiConfiguration {

    @Bean
    @Autowired
    public OddsApiService oddsApiService(RestClient restClient) {
        RestClientAdapter adapter = RestClientAdapter.create(restClient);
        HttpServiceProxyFactory factory = HttpServiceProxyFactory.builderFor(adapter).build();

        return factory.createClient(OddsApiService.class);
    }
}
