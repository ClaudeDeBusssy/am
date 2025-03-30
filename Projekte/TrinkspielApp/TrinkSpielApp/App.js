import React from "react";
import { SafeAreaView, View, StyleSheet } from "react-native";
import WelcomeScreen from "./app/screens/WelcomeScreen";
import SelectScreen from "./app/screens/SelectScreen";

import colors from "./app/config/colors";

export default function App() {
  return (
    <SafeAreaView style={styles.container}>
      <WelcomeScreen />
      {/* <SelectScreen></SelectScreen> */}
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: colors.bgTest,
  },
});
