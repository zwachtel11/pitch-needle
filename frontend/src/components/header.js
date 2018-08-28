import React from 'react'
import { Link } from 'gatsby'
import {
  Container,
  Divider,
  Dropdown,
  Grid,
  Header,
  Image,
  List,
  Menu,
  Segment,
} from 'semantic-ui-react'

const Header1 = ({ siteTitle }) => (
  <div
  >
    <Menu fixed='top' inverted>
      <Container>
        <Menu.Item as='a' header>
          { siteTitle }
        </Menu.Item>
      </Container>
</Menu>
  </div>
)

export default Header1
