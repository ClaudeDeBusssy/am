import React from "react";
import { Text, View, StyleSheet, TouchableOpacity } from "react-native";

import colors from "../config/colors";

function SelectScreen({ navigation }) {
  const goToSelectScreen = () => {
    console.log("Start Button Pressed")
    navigation.navigate('Play');
  };

  return (
    <View>
      <Text>Select Screen</Text>
      <TouchableOpacity style={styles.startButton} onPress={goToSelectScreen} >

        <View style={styles.startButtonView} ><Text style={styles.startButtonText} >START</Text></View>
      </TouchableOpacity>
    </View>);
}

const styles = StyleSheet.create({

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
  }
});

export default SelectScreen;
