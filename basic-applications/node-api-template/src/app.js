const express = require("express"); 
const Router = require("./routes");

const app = express(); 
const PORT = process.env.PORT || 3000; 


app.use("/api/", Router);

app.listen(PORT, () => { 
    console.log(`API is listening on port ${PORT}`); 
});