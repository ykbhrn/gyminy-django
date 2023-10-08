import React from 'react'
import { getAllSports } from '../../lib/api'


class SportSelect extends React.Component {

  state = {
    sports: null
  }

  async componentDidMount() {
    try {
      const res = await getAllSports()
      this.setState({ sports: res.data })
    } catch (err) {
      console.log(err)
    }
  }


  render() {
    // if (!this.state.sports) return null
    return (
      <div className="select is-multiple">
        <select multiple size="3"
          onClick={this.props.handleSelect}
          name="sports"
        >
          <option>Aerobic</option>
          <option>Yoga</option>
          <option>Strength and Conditioning</option>
          <option>Combat Sports</option>
          <option>Powerlifting</option>
          <option>Weightlifting</option>
          <option>Breathing Exercises</option>
        </select>
      </div>
    )
  }

}
export default SportSelect