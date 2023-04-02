import * as React from 'react';
import "./styles/App.css"

const App = () => {
  const title = 'TC Walkie Talkie';
  const description = ['A walkie talkie application. Speak to other nodes on the network.',
                      ' Use the dial to choose a channel and use the switch to record audio. ',
                      ' You can not hear while talking and will only communicate with nodes on the same channel.']

  return (
    <div className='container'>
      <a> 
        <img
          src="./images/tc_logo_transparent.png" style={{width : 250}}>

        </img>
      </a>
      <h1>
        {title}
      </h1>
      <p>
        {description}
      </p>
    </div>
  );
}

export default App;