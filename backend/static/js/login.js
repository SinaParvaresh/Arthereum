window.userWalletAddress = null;
const loginButton = document.getElementById('loginButton');

function toggle () {
  if (typeof window.ethereum === 'undefined') {
    loginButton.innerText = 'Please install MetaMask first';

    console.log("metaMask not found!");
    return false;
  }

  let con = false;
  const { ethereum } = window;
  if (ethereum) {
    var provider = new ethers.providers.Web3Provider(ethereum);
  }

  async function isMetaMaskConnected() {
      const accounts = await provider.listAccounts();
      con = accounts.length > 0;
      window.userWalletAddress = accounts[0];
      return con;
    }

    if (isMetaMaskConnected())
    {
      var data = {address : window.userWalletAddress};

      const request = new XMLHttpRequest(0);
      console.log(window.userWalletAddress);
      request.open('GET', `login?address=${window.userWalletAddress}`, true);
      request.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
      request.onload = () => {
        const data = JSON.parse(request.responseText);
        console.log(data);
      }

      request.send(data);
      load_form('login');
    }
    else {
      load_form('connect');
    }

  console.log("metaMask found");
  loginButton.addEventListener('click', loginWithMetaMask);
}

async function loginWithMetaMask() {
  const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' })
        .catch((e) => {
          console.error(e.message);
          return;
        })
      if (!accounts) { return; }

    window.userWalletAddress = accounts[0];
    console.log(accounts[0]);
      return false;

    /*
    loginButton.innerText = 'Connected!! Please proceed...'
    loginButton.removeEventListener('click', loginWithMetaMask);
      setTimeout(() => {
        loginButton.addEventListener('click', () => {
          load_form('login');
        });
      }, 200);
      */
}

function load_form(form) {
  if (form == "login")
  {
    document.querySelector('#login_password').style.display = 'block';
    document.querySelector('#login_username').style.display = 'block';
    document.querySelector('#login_button').style.display = 'block';
    loginButton.style.display = 'none';
    console.log("login form");

    $.ajax({
        url: 'login/',
        type: 'GET',
        data: data,
        dataType: 'json',
        success: function (data) {
          console.log(data);
        }
      });
  }
  else if (form == "connect")
  {
    document.querySelector('#login_password').style.display = 'none';
    document.querySelector('#login_username').style.display = 'none';
    document.querySelector('#login_button').style.display = 'none';
    console.log("Metamask Form");
  }
}

window.addEventListener('DOMContentLoaded', function() {
  toggle();
});
