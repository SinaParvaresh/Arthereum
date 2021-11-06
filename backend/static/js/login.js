window.userWalletAddress = null;
const loginButton = document.getElementById('loginButton');

function checkMetaMask() {
  if (typeof window.ethereum === 'undefined') {
    loginButton.innerText = 'Please install MetaMask first';

    console.log("metaMask not found!");
    return false;
  }

  if (window.userWalletAddress === null)
  {
    document.querySelector('#login_password').style.display = 'none';
    document.querySelector('#login_username').style.display = 'none';
    document.querySelector('#login_button').style.display = 'none';
  }
  else
  {
    document.querySelector('#createAccount').style.display = 'none';
    document.querySelector('#metaconnect').style.display = 'none';
    document.querySelector('#login_password').style.display = 'block';
    document.querySelector('#login_username').style.display = 'block';
    document.querySelector('#login_button').style.display = 'block';
  }

  loginButton.addEventListener('click', loginWithMetaMask)
}

async function loginWithMetaMask() {
  const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' })
        .catch((e) => {
          console.error(e.message);
          return;
        })
      if (!accounts) { return; }

    window.userWalletAddress = accounts[0];
    //console.log(accounts[0]);

      loginButton.removeEventListener('click', loginWithMetaMask)
      setTimeout(() => {
        loginButton.addEventListener('click', signOutOfMetaMask)
      }, 200);
}

function signOutOfMetaMask() {
      window.userWalletAddress = null;
      userWallet.innerText = '';
      loginButton.innerText = 'Sign in with MetaMask';

      loginButton.removeEventListener('click', signOutOfMetaMask)
      setTimeout(() => {
        loginButton.addEventListener('click', loginWithMetaMask)
      }, 200);
    }

    window.addEventListener('DOMContentLoaded', () => {
      checkMetaMask();
    });
