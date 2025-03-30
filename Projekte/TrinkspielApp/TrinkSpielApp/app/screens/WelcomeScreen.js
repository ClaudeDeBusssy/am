import React from "react";
import { Image, ImageBackground, StyleSheet, Text, View, TouchableOpacity } from "react-native";

import colors from "../config/colors";

function WelcomeScreen({ navigation }) {
  const goToSelectScreen = () => {
    console.log("Start Button Pressed")
    navigation.navigate('Select');
  };

  return (
    <ImageBackground
      style={styles.background}
      source={require("../assets/icon.png")}
    >
      <View style={styles.logoContainer}>
        <Image
          style={styles.logo}
          source={require("../assets/BierLogo.webp")}
        ></Image>
        <Text style={styles.startButtonText} >Trinkspiel</Text>
      </View>
      <TouchableOpacity style={styles.startButton} onPress={goToSelectScreen} >

        <View style={styles.startButtonView} ><Text style={styles.startButtonText} >START</Text></View>
      </TouchableOpacity>
    </ImageBackground>
  );
}

const styles = StyleSheet.create({
  background: {
    flex: 1,
    justifyContent: "flex-end",
    alignItems: "center",
  },
  startButton: {
    backgroundColor: colors.secondary,
    width: "90%",
    height: 150,
    bottom: 50,
  },
  startButtonView: {
    flexGrow: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  startButtonText: {
    fontFamily: 'Apple SD Gothic Neo',
    fontSize: 75,
    fontWeight: "bold"
  },
  logo: {
    width: 300,
    height: 300,
  },
  logoContainer: {
    position: "absolute",
    top: 150,
    alignItems: "center",
  },
});

export default WelcomeScreen;
