<?php

namespace App\Http\Controllers;

use Symfony\Component\Process\Exception\ProcessFailedException;
use Symfony\Component\Process\Process;

class BotController extends Controller
{
    public function __invoke($user_input)
    {
        // Path to the Python script
        $scriptPath = storage_path('/app/gemini.py');
        $apiKey = env('GENAI_API_KEY');
        $pythonPath = env('PYTHON_PATH');
        
        // Command to run the script with the API key and user input
        $process = new Process([$pythonPath, $scriptPath, $apiKey, $user_input]);

        try {
            $process->mustRun();
            $output = $process->getOutput();
            return response()->json([
                'success' => true,
                'message' => $output,
            ]);
        } catch (ProcessFailedException $exception) {
            return response()->json([
                'success' => false,
                'error' => $exception->getMessage(),
            ], 500);
        }
    }
}