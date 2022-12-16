import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <a
          className="App-link"
          href="http://localhost:8000/login/"
          target="_blank"
          rel="noopener noreferrer"
        >
          Login
        </a>
        <a
          className="App-link"
          href="http://localhost:8000/logout/"
          target="_blank"
          rel="noopener noreferrer"
        >
          Logout
        </a>
      </header>
    </div>
  );
}

export default App;
