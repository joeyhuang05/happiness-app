import Ionicons from '@expo/vector-icons/Ionicons';
import { StyleSheet, Image, Platform } from 'react-native';

import { Collapsible } from '@/components/Collapsible';
import { ExternalLink } from '@/components/ExternalLink';
import ParallaxScrollView from '@/components/ParallaxScrollView';
import { ThemedText } from '@/components/ThemedText';
import { ThemedView } from '@/components/ThemedView';

import React from 'react';

import splashBack from './splash.png';
import logo from './logo.png';

class SplashScreen extends React.Component {
    constructor(props: {}) {
        super(props);
        this.state = {
        };
    }

    render() {
        return (
            <img src={splashBack} alt="Splash Screen"> 
                <img src={logo} alt = "Logo" />
            </img>
        )
    }
}