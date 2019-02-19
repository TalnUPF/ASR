/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.upf.taln.asr;

import java.io.File;
import java.nio.charset.Charset;
import org.apache.commons.io.FileUtils;

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
        String resultDir = "C:\\Users\\U96153\\Documents\\NetBeansProjects\\Sphinx\\src\\main\\resources\\results\\en\\";
        File[] dir = new File(pathDir).listFiles();
        for(File f : dir)
        {
            String name = f.getName();
            int idF = Integer.parseInt(name.split("_")[1].split("\\.")[0]);
            String spkInfo = name.split("_")[0];
            String pathOut = resultDir+spkInfo+"_"+idF+".txt";
            File outFile = new File(pathOut);

            if(outFile.exists())
            {
                System.out.println(pathOut+"\nHave it, skipping");
            }
            else
            {
                String transcription = t.speechToText(f);
                FileUtils.writeStringToFile(outFile, transcription, Charset.forName("UTF-8"));
            }
            
        }
    }
}
