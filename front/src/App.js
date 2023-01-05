import React, { Component } from 'react';

class App extends Component {
    state = {
        posts: []
    };

    async componentDidMount() {
        try {
            const res = await fetch('http://127.0.0.1:8000/posts/');
            console.log(res)
            const posts = await res.json();
            this.setState({
                posts
            });
        } catch (e) {
            console.log(e);
        }
    }

    render() {
        return (
            <div>
                {this.state.posts.map(item => (
                    <div key={item.pk}>
                        <h1>{item.title}</h1>
                        <p>{item.body}</p>
                        <img src={item.image} alt = "default"/>
                        <p>{item.published_date}</p>
                    </div>
                ))}
            </div>
        );
    }
}

export default App;