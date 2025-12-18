package day11

import (
	"fmt"
	"strings"
)

const Title string = "Reactor"

const p1Start string = "you"
const DAC string = "dac"
const FFT string = "fft"
const OUT string = "out"

type Device struct {
	Name    string
	Outputs []string
}

type Packet struct {
	startDevice Device
	outCount    int
	foundDac    bool
	foundFft    bool
}

func traceRoute(packet *Packet, devices map[string]Device) {
	for _, deviceName := range packet.startDevice.Outputs {
		switch deviceName {
		case OUT:
			// NOTE: since the "out" device always seems to be the last in
			// a device's output list, THERE's NO need to short circuit
			// the search once a path has been found
			packet.outCount += 1
		case DAC:
			packet.foundDac = true
		case FFT:
			packet.foundFft = true
		}

		packet.startDevice = devices[deviceName]
		traceRoute(packet, devices)
	}
}

func solvePart1(devices map[string]Device) int {
	var packet Packet = Packet{
		startDevice: devices[p1Start],
		outCount:    0,
		foundDac:    false,
		foundFft:    false,
	}

	traceRoute(&packet, devices)

	return packet.outCount
}

func solvePart2(devices map[string]Device) int {
	return 0
}

func processInput(data []string) map[string]Device {
	// ccc: ddd eee fff
	devices := map[string]Device{}

	for _, line := range data {
		name, outStr, _ := strings.Cut(line, ":")
		outputs := strings.Split(strings.TrimSpace(outStr), " ")
		devices[name] = Device{name, outputs}
	}

	return devices
}

func Exec(part string, data []string) (int, error) {
	var result int = 0
	var err error = nil

	devices := processInput(data)

	if part == "PART1" {
		result = solvePart1(devices)
	} else if part == "PART2" {
		result = solvePart2(devices)
	} else {
		err = fmt.Errorf("Day11 - Unknown Part: [%s]\n", part)
	}

	return result, err
}
