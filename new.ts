function Greetings(): void {
  const readline = require('readline');
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  rl.question("Enter your name: ", (User: string) => {
    console.log(`Hi, ${User}`);
    rl.close();
  });
}

Greetings();