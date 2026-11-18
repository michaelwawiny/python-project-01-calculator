const display = document.getElementById("display");

function appendValue(value) {
  if (display.value === "0" || display.value === "Error") {
    display.value = value;
  } else {
    display.value += value;
  }
}

function clearDisplay() {
  display.value = "0";
}

function deleteLast() {
  display.value = display.value.slice(0, -1);

  if (display.value === "") {
    display.value = "0";
  }
}

function calculateResult() {
  try {
    const expression = display.value;

    // Only allow basic mathematical expressions.
    if (!/^[0-9+\-*/%.()\s]+$/.test(expression)) {
      throw new Error("Invalid expression");
    }

    const result = Function('"use strict"; return (' + expression + ")")();

    if (typeof result !== "number" || !Number.isFinite(result)) {
      throw new Error("Invalid calculation");
    }

    display.value = Number(result.toFixed(10)).toString();
  } catch (error) {
    display.value = "Error";
  }
}
