import React from 'react';

class Main extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      answers: '',
    };

    this.handleUploadImage = this.handleUploadImage.bind(this);
  }

  handleUploadImage(ev) {
    ev.preventDefault();

    let data = new FormData();
    data.append('file', this.uploadInput.files[0]);

    fetch('https://pod-matcher.herokuapp.com/api/upload', {
        method: 'POST',
        // mode: 'no-cors',
        body: data,
        "Access-Control-Allow-Origin" : "*", 
        "Access-Control-Allow-Credentials" : true })
  .then(response => response.json())
  .then(data => console.log(data));
  }

  render() {
    return (
      <form onSubmit={this.handleUploadImage}>
        <div>
          <input ref={(ref) => { this.uploadInput = ref; }} type="file" />
        </div>
        <br />
        <div>
          <button>Upload</button>
        </div>
        <h1>
        {this.state.answers}
          </h1>
      </form>
    );
  }
}

export default Main;