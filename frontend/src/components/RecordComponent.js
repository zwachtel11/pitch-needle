import React from "react";
import { Card, Icon, Image, Header, Dimmer, Button } from 'semantic-ui-react'
/**
const RecordComponent = (props) => {
    return (
        <Card href='http://google.com'>
        <Image src={props.cover} 
         />
        <Card.Content>
          <Card.Header>{props.album}</Card.Header>
          <Card.Meta>
            <span className='date'>{props.genre}</span>
          </Card.Meta>
          <Card.Description>{props.artist}</Card.Description>
        </Card.Content>
        <Card.Content extra>
          <a>
            <Icon name='user' />
            {props.provider}
          </a>
        </Card.Content>
      </Card>
    )
}
 */
class RecordComponent extends React.Component {
    constructor() {
        super();
        this.state = {}
    }
    handleShow = () => this.setState({ active: true })
    handleHide = () => this.setState({ active: false })

    render() {
        const { active } = this.state
        const content = (
          <div>    
            <Button inverted color='green' as='a' href={this.props.applelink}>Apple Music</Button>
            <Button inverted color='green'>Spotify</Button>
          </div>
        )
    
        return (
        <Card>
          <Dimmer.Dimmable
            as={Image}
            dimmed={active}
            blurring
            dimmer={{ active, content }}
            onMouseEnter={this.handleShow}
            onMouseLeave={this.handleHide}
            size='medium'
            src={this.props.cover}
          />
          <Card.Content>
            <Card.Header>{this.props.album}</Card.Header>
            <Card.Meta>
              <span className='date'>{this.props.genre}</span>
            </Card.Meta>
            <Card.Description>{this.props.artist}</Card.Description>
          </Card.Content>
          <Card.Content extra>
            <a>
              <Icon name='user' />
              {this.props.provider}
            </a>
          </Card.Content>
        </Card>
        )
      }
}

export default RecordComponent