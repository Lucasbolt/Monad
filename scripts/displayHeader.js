const sleep = require("./sleep");

module.exports = (async () => {
    process.stdout.write("\x1Bc");
    console.log("========================================".magenta);
    console.log("=          Monad Testnet Bot           =".magenta);
    console.log("=        Created by lucasbolt          =".magenta);
    console.log("=       https://x.com/BankendGuy       =".magenta);
    console.log("========================================".magenta);
    console.log();
    return await sleep(1)
});
