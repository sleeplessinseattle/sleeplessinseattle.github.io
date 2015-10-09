import os
import main

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    main.app.run(host='0.0.0.0', port=port, debug=os.environ.get('DEBUG', False))