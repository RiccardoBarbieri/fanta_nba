package com.betapi.database.repositories;

import com.betapi.database.documents.Bookmaker;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;
import org.springframework.stereotype.Repository;

@Repository("bookmakerRepository")
public interface BookmakerRepository extends MongoRepository<Bookmaker, String> {

//    @Query("{ 'key' : ?0 }")
    Boolean existsByKey(String key);
}
