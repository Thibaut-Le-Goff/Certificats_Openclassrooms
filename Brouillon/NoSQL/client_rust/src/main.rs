use mongodb::{Client, options::{ClientOptions, ResolverConfig}, bson::doc, error::Result};
use std::env;
use std::error::Error;
use tokio;
use std::process::Command;

/*
 source : https://www.mongodb.com/developer/languages/rust/rust-mongodb-crud-tutorial/
        : https://mongodb.github.io/mongo-rust-driver/manual/index.html
 to run :
 RUST_LOG='mongodb::command=debug' MONGODB_URI=mongodb://172.0.0.2:27017 cargo run
*/

#[tokio::main]
async fn main() -> Result<()> {
   env::set_var("RUST_BACKTRACE", "0");

   tracing_subscriber::fmt::init();

   let client_uri = env::var("MONGODB_URI").expect("You must set the MONGODB_URI environment var!");
   println!("mongodb_uri: {}", client_uri);

   let client = Client::with_uri_str(client_uri).await?;
   println!("client: {:?}", client);

   /* 
   for i in 0..5 {
      let client_ref = client.clone();

      task::spawn(async move {
         let collection = client_ref.database("items").collection::<Document>(&format!("coll{}", i));

         // Do something with the collection
      });
   }

   println!("Databases:");
   for name in client.list_database_names(None, None).await? {
      println!("- {}", name);
   }*/

   Ok(())
}
