package shared

type Direction struct {
	RowOffset int
	ColOffset int
}

var N Direction = Direction{-1, +0}
var NE Direction = Direction{-1, +1}
var E Direction = Direction{+0, +1}
var SE Direction = Direction{+1, +1}
var S Direction = Direction{+1, +0}
var SW Direction = Direction{+1, -1}
var W Direction = Direction{+0, -1}
var NW Direction = Direction{-1, -1}

var Directions []Direction = []Direction{N, NE, E, SE, S, SW, W, NW}
