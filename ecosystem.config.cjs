module.exports = {
    apps: [
      {
        name: 'node-server',
        script: '.output/server/index.mjs',
        instances: 1,
        exec_mode: 'fork',
      },
      {
        name: 'tuna-backends',
        script: 'tuna',
        args: 'http 8000 --subdomain=backends',
        instances: 1,
        exec_mode: 'fork',
      },
      {
        name: 'tuna-tessst',
        script: 'tuna',
        args: 'http 3000 --subdomain=tessst',
        instances: 1,
        exec_mode: 'fork',
      },
    ],
  };
  