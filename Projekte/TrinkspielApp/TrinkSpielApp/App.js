import React from "react";
import { SafeAreaView, View, StyleSheet } from "react-native";
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import WelcomeScreen from "./app/screens/WelcomeScreen";
import SelectScreen from "./app/screens/SelectScreen";
import PlayScreen from "./app/screens/PlayScreen";


import colors from "./app/config/colors";

export default function App() {
  return (
    <SafeAreaView style={styles.container}>
      <NavigationContainer >
        <Stack.Navigator initialRouteName="Welcome">
          <Stack.Screen name="Welcome" component={WelcomeScreen} options={{ headerShown: false }} />
          <Stack.Screen name="Select" component={SelectScreen} options={{ headerShown: false }} />
          <Stack.Screen name="Play" component={PlayScreen} options={{ headerShown: false }} />

        </Stack.Navigator>
      </NavigationContainer>
      {/* <WelcomeScreen /> */}
      {/* <SelectScreen></SelectScreen> */}
    </SafeAreaView>
  );
}


const Stack = createStackNavigator();

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: colors.bgTest,
  },
});
