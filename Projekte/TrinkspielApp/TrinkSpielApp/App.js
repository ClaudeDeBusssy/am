import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Image, SafeAreaView } from 'react-native';

export default function App() {
  const handlePress = () => console.log('Text Pressed');

  return (
    <SafeAreaView style={styles.container}>
      <Text onPress={handlePress}>Diese App wird super</Text>
      <Text>Zweiter Text</Text>
      <Image source={{
        width: 200,
        height: 200,
        uri: "https://picsum.photos/200/200"
      }}></Image>



      <StatusBar style="auto" />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0ff',
    justifyContent: 'center',
    alignItems: 'center'
  },
});
