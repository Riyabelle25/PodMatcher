import React from "react";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";

import styles from '../styles/main.module.css';

class Main extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      answers: "",
      set: false,
    };

    this.handleUploadImage = this.handleUploadImage.bind(this);
  }

  createData(name, percentage) {
    return { name, percentage };
  }

  handleUploadImage(ev) {
    ev.preventDefault();

    let data = new FormData();
    data.append("file", this.uploadInput.files[0]);

    fetch("https://pod-matcher.herokuapp.com/api/upload", {
      method: "POST",
      // mode: 'no-cors',
      body: data,
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Credentials": true,
    })
      .then((response) => response.json())
      .then((data) => {
        const results = data.data;
        var answers = [];

        for (var i in results) {
          answers.push(this.createData(results[i][0], results[i][1]));
        }
        console.log(answers);
        console.log(results);
        this.setState({ answers: answers, set: true });
      });
  }

  render() {
    return (
      <form onSubmit={this.handleUploadImage}>
        <div className={styles.wrapper}>
          <input className={styles.fileInput}
            ref={(ref) => {
              this.uploadInput = ref;
            }}
            type="file"
          />
        </div>
        <br />
        <div>
          <button type="submit" className={styles.matchCandidates}>Match Candidates!</button>
        </div>
        {this.state.set && (
          <TableContainer component={Paper}>
            <Table sx={{ minWidth: 650 }} aria-label="simple table">
              <TableHead>
                <TableRow>
                  <TableCell>Name</TableCell>
                  <TableCell align="right">Match</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {this.state.answers.map((row) => (
                  <TableRow
                    key={row.name}
                    sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
                  >
                    <TableCell component="th" scope="row">
                      {row.name}
                    </TableCell>
                    <TableCell align="right">{row.percentage}</TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>
        )}
      </form>
    );
  }
}

export default Main;
