/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.upf.taln.asr;

import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;

import edu.cmu.sphinx.api.Configuration;
import edu.cmu.sphinx.api.SpeechResult;
import edu.cmu.sphinx.api.StreamSpeechRecognizer;
import edu.cmu.sphinx.decoder.adaptation.Stats;
import edu.cmu.sphinx.decoder.adaptation.Transform;
import edu.cmu.sphinx.result.WordResult;

/**
 * A simple example that shows how to transcribe a continuous audio file that
 * has multiple utterances in it.
 */
public class TranscriberDemo {

    public static void main(String[] args) throws Exception 
    {
        String LANG = "en";
        Transcriber t = new Transcriber(LANG);
        String pathDir = "C:\\Users\\U96153\\Documents\\NetBeansProjects\\Sphinx\\src\\main\\resources\\audios\\en";
        
        File[] dir = new File(pathDir).listFiles();
        for(File f : dir)
        {
            System.out.println(f.getAbsoluteFile().toString());
            System.out.println(t.speechToText(f));
        }
    }
}
