if (typeof window.ethereum !== 'undefined') {
  console.log("Metamask Installed");
} else {
  console.log("Install Metamask");
}


const ethereumButton = document.querySelector('.enableEthereumButton');
const showAccount = document.querySelector('.showAccount');
const sendEthButton = document.querySelector('.sendEthButton');
const showBalance = document.querySelector('.showBalance');

ethereumButton.addEventListener('click', () => {
  getAccount();
})


async function getAccount(){
  const accounts = await ethereum.request({method: 'eth_requestAccounts'});
  const account = accounts[0];
  showAccount.innerHTML = account;

  const balance = await ethereum
  .request({
    method: 'eth_getBalance',
    params: [account, "latest"]
  });

  const read = parseInt(balance) / 10**18;
  console.log(read.toFixed(5));
  showBalance.innerHTML = read.toFixed(5);

  sendEthButton.addEventListener('click', () => {
    ethereum
      .request({
        method: 'eth_sendTransaction',
        params:[
          {
            from: account,
            to: '0x261B3C9a2bf8E501aE6fB69De8cDD187320eac69', // adress of the account to be sent
          }
        ],
      })
      .then((txHash) => console.log(txHash))
      .catch((error) => console.console.error);
  });
}


