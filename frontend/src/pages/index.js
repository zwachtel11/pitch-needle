import React from 'react'
import { Link } from 'gatsby'
import axios from "axios";
import { Grid, Container } from 'semantic-ui-react'
import InfiniteScroll from 'react-infinite-scroller';
import Layout from '../components/layout'
import RecordComponent from '../components/RecordComponent'

class IndexPage extends React.Component {
  constructor() {
    super();
    this.state = {
        records: [],
        partRec:[]
    }
}
  loadFunc() {
/**
    var test = []
    var i = 0;
    while (i < 10)
    {
      test.push(this.state.records[i])
      i++
    }
    this.setState((()=>{
      return {
        partRec: test
      }
    }))
 */
  }

  componentDidMount(){
    axios.get("http://localhost:5000/api/record").then((response)=>{
        console.log("response.data")
        this.setState((()=>{
          return {
            records: response.data
          }
        }))
    })
  }
  render() {
    let mappedRecords = this.state.records.map((record)=>{
      return (
              <Grid.Column>
                <RecordComponent album={record.album}
                    artist={record.artist}
                   provider={record.provider}
                   cover={record.cover}
                   genre={record.genre}
                   applelink={record.appleLink}
                   />
              </ Grid.Column>
    )
    })
    return (
      <Layout >
        <Container style={{ marginTop: '6em' }}>
        <InfiniteScroll
        pageStart={0}
        loadMore={this.loadFunc.bind(this)}
        hasMore={true|| false}
        loader={<div className="loader" key={0}>Loading ...</div>}
        >
      <Grid columns={3}>
      {mappedRecords}
      </ Grid>
      </InfiniteScroll>
      </ Container>
      <Link to="/page-2/">Go to page 2</Link>
    </Layout>
    )
  }
}

export default IndexPage
