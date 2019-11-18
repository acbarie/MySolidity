var ethers = require('ethers');
var rndwallet = ethers.Wallet.createRandom();
const fs = require('fs');

let rawdata = fs.readFileSync('mywallet.json');
let encwallet = JSON.parse(rawdata);

console.log(encwallet);

function callback(progress) {
    //console.log("Encrypting: " + parseInt(progress * 100) + "% complete");
    process.stdout.write("Decrypting: " + parseInt(progress * 100) + "% complete\r");
}

var json = JSON.stringify(encwallet);
var password = "password123";
ethers.Wallet.fromEncryptedJson(json, password, callback).then(function(wallet) {
    console.log("Address: " + wallet.address);
    // "Address: 0x88a5C2d9919e46F883EB62F7b8Dd9d0CC45bc290"
});
