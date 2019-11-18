var ethers = require('ethers');

//create a random wallet
let randomWallet = ethers.Wallet.createRandom();
console.log("Address: " + randomWallet.address);
var privkey = randomWallet.privateKey;
console.log("privatekey: " + privkey);


//encrypt the wallet
console.log("encrypting");
let password = "password123";
function callback(progress) {
    //console.log("Encrypting: " + parseInt(progress * 100) + "% complete");
    process.stdout.write("Encrypting: " + parseInt(progress * 100) + "% complete\r");
}

var jsondata = ""
let encryptPromise = randomWallet.encrypt(password, callback);
encryptPromise.then(function(jsondata) {
    console.log(jsondata);
	const fs = require('fs');
	//let data = JSON.stringify(jsondaa);
	fs.writeFileSync('mywallet.json', jsondata);
});

