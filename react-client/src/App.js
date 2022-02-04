import './App.css';
import React from 'react'
import Main from './components/fileUpload'

const App = () => (
  <div>
    <h1>Pod-Matcher</h1>
    <p>To build a Pod, you must first upload the Requirements that the Mentees in your Pod should have. </p>

    <p>
      This describes the skill sets, languages, time zones, and other factors the PodMatcher should consider while forming your dream Pod. 
      The Flask server sends a request to the Firestore Database, which retrieves all of the applications, and then uses 
      BoW and TF-IDF for vectorization and cosines similarity for comparison to provide a percentage-wise list of likely applicants. 
      This App is built using React, and is therefore responsive across devices.</p>
    <Main />
  </div>
);
export default App;
