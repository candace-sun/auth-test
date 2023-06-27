import logo from "./logo.svg";
import "@aws-amplify/ui-react/styles.css";
import {
  withAuthenticator,
  Button,
  Heading,
  Image,
  View,
  Card,
} from "@aws-amplify/ui-react";


import UploadButton from './components/upload-button.js';
import axios from 'axios';
import React, { useState } from 'react';
import './App.css';


function App({ signOut, user }) {
  const [files, setFiles] = useState([null, null, null, null, null]);

  function test() {
    console.log(files);

    var myParams = {
      data: "testing"
    }

    // check if all files are present:

    axios.post('http://3.210.118.177/new', myParams)
      .then(function (response) {
        console.log(response);
        //Perform action based on response
        let result = response.data;
        console.log(result);
      })
      .catch(function (error) {
        console.log(error);
        //Perform action based on error
      });
  }

  return (
    <View>
      <div className="Header">
        <div>Welcome <b>{user.username}</b>!</div>
        <Button onClick={signOut}>Sign Out</Button>
      </div>

      <div className="App">
        <div className="Left-new">
          <h2 className="App-header">
            Import New Run
          </h2>
          <div className="Button-grid">
            <UploadButton label={'Scenic File (.scenic)'} fileType={'.scenic'} id={0}
              pState={{ files, setFiles }} />
            <UploadButton label={'Launch File (.launch/.xlaunch)'} fileType={'.launch,.xlaunch'} id={1}
              pState={{ files, setFiles }} />
            <UploadButton label={'ROS Bag Analysis Script (.py)'} fileType={'.py'} id={2}
              pState={{ files, setFiles }} />
            <UploadButton label={'Navigation Waypoints (.py/.yaml)'} fileType={'.py, .yaml'} id={3}
              pState={{ files, setFiles }} />
            <UploadButton label={'Time-of-day (.yaml)'} fileType={'.yaml'} id={4} pState={{ files, setFiles }} />

            <div>
              <Button onClick={test}>Start Run</Button>

            </div>
          </div>
        </div>
        <div className="Right-view">
          <h2 className="App-header">
            View Existing Runs
          </h2>

        </div>
      </div>
    </View>
  );
}

export default withAuthenticator(App);