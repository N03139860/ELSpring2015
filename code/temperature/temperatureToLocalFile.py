#!/usr/bin/python
import temperature

temperature = temperature.Temperature()

listOfTemperatures = temperature.getListOfTemperatures(20, 5)
temperature.printToCsvFile(listOfTemperatures, 'output_for_local_file.csv')
