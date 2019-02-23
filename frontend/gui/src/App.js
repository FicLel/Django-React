import React, { Component } from 'react';
import './App.css';
import Articles from './components/Articles';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
        
          <Articles/>
        </header>
      </div>
    );
  }
}

export default App;
