package betapi.database.repositories;

import betapi.database.documents.Bookmaker;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

@Repository("bookmakerRepository")
public interface BookmakerRepository extends MongoRepository<Bookmaker, String> {

//    @Query("{ 'key' : ?0 }")
    Boolean existsByKey(String key);
}
