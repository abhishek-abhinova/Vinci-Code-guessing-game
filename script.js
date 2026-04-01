let numPlayers = 0;
let players = {};
let currentPlayer = 1;
let turn = 0;
let moveHistory = [];
const board = Array(18).fill(null); // spots 1 to 17

const colors = ['player-color-1', 'player-color-2', 'player-color-3', 'player-color-4', 'player-color-5'];

function startGame() {
  numPlayers = parseInt(document.getElementById('numPlayers').value);
  if (isNaN(numPlayers) || numPlayers < 2 || numPlayers > 5) {
    alert("Please enter a number between 2 and 5.");
    return;
  }

  // Get player names
  players = {};
  for (let i = 1; i <= numPlayers; i++) {
    const nameInput = document.getElementById(player${i});
    const name = nameInput ? nameInput.value || Player${i} : Player${i};
    players[i] = {
      name: name,
      symbol: P${i},
      color: colors[i - 1],
      points: 0
    };
  }

  document.getElementById('player-setup').style.display = 'none';
  document.getElementById('game').style.display = 'block';
  drawBoard();
  updateDisplay();
}

function drawBoard() {
  const boardDiv = document.getElementById('board');
  boardDiv.innerHTML = "";

  for (let i = 1; i <= 17; i++) {
    const spot = document.createElement("div");
    spot.classList.add("spot");
    spot.setAttribute("data-id", i);
    if (board[i]) {
      const player = players[board[i]];
      spot.innerHTML = <span class="${player.color}">${player.symbol}</span>;
    } else {
      spot.innerHTML = i;
    }
    spot.onclick = () => placePiece(i);
    boardDiv.appendChild(spot);
  }
}

function placePiece(index) {
  if (board[index]) {
    alert("Spot already taken!");
    return;
  }

  if (index === 9 && !validSpot9(currentPlayer)) {
    alert("To play on spot 9, you must form a line!");
    return;
  }

  board[index] = currentPlayer;
  moveHistory.push(index);
  turn++;

  updateScores();
  if (turn === 17) {
    endGame();
    return;
  }

  currentPlayer = (turn % numPlayers) + 1;
  drawBoard();
  updateDisplay();
}

function undoMove() {
  if (!moveHistory.length) {
    alert("No moves to undo.");
    return;
  }

  const lastMove = moveHistory.pop();
  board[lastMove] = null;
  turn--;
  currentPlayer = (turn % numPlayers) + 1;
  drawBoard();
  updateScores();
  updateDisplay();
}

function updateDisplay() {
  const turnDisplay = document.getElementById("turnDisplay");
  turnDisplay.innerHTML = ${players[currentPlayer].name}'s turn (${players[currentPlayer].symbol});

  const scoreDisplay = document.getElementById("scoreDisplay");
  scoreDisplay.innerHTML = "";
  for (let i = 1; i <= numPlayers; i++) {
    scoreDisplay.innerHTML += ${players[i].name} (${players[i].symbol}): ${players[i].points} points<br>;
  }
}

function updateScores() {
  for (let p = 1; p <= numPlayers; p++) {
    let pts = 0;

    const isMatch = (combo) => combo.every(i => board[i] === p);

    const lines = [
      [1, 2, 3], [4, 5, 6], [7, 8, 9], [12, 13, 14], [15, 16, 17],
      [1, 5, 11], [2, 5, 10], [3, 6, 11], [7, 12, 15], [8, 13, 16], [9, 14, 17],
      [1, 4, 9], [3, 5, 9], [7, 13, 17], [9, 13, 15], [8, 9, 10], [9, 10, 11], [4, 9, 14], [5, 9, 13]
    ];

    const triangles = [
      [1, 2, 5], [1, 4, 5], [2, 3, 5], [5, 6, 3], [8, 9, 4], [4, 5, 10],
      [13, 14, 16], [13, 12, 15], [7, 8, 13], [9, 13, 14]
    ];

    const squares = [
      [1, 2, 4, 5], [3, 2, 6, 5], [4, 9, 5, 10], [5, 10, 6, 11],
      [7, 8, 13, 12], [8, 9, 13, 14], [12, 13, 16, 15], [13, 14, 16, 17]
    ];

    lines.forEach(combo => { if (isMatch(combo)) pts += 3; });
    triangles.forEach(combo => { if (isMatch(combo)) pts += 1; });
    squares.forEach(combo => { if (isMatch(combo)) pts -= 2; });

    players[p].points = pts;
  }
}

function validSpot9(p) {
  const tempBoard = [...board];
  tempBoard[9] = p;
  const lines = [
    [1, 4, 9], [10, 8, 9], [9, 10, 11], [9, 14, 17],
    [7, 8, 9], [3, 5, 9], [14, 4, 9], [9, 13, 15], [5, 9, 13]
  ];
  return lines.some(line => line.every(i => tempBoard[i] === p));
}

function endGame() {
  alert("End game phase — final scores will be calculated!");
  updateScores();
  drawBoard();

  let maxPoints = Math.max(...Object.values(players).map(p => p.points));
  let winners = Object.values(players).filter(p => p.points === maxPoints);

  if (winners.length === 1) {
    alert(🏆 Winner: ${winners[0].name} with ${winners[0].points} points!);
  } else {
    alert(🤝 It's a tie between: ${winners.map(w => w.name).join(", ")});
  }
}