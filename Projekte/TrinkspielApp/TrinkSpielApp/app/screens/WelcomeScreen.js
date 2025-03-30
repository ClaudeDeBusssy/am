import React from "react";
import { Image, ImageBackground, StyleSheet, Text, View } from "react-native";

import colors from "../config/colors";

function WelcomeScreen(props) {
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
        <Text>Trinskpiel</Text>
      </View>
      <View style={styles.startButton}>
        <Text>Starten</Text>
      </View>
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
