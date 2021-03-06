package com.example.firstapp;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity
{

    private Button day, month, info, options, disclaimer;

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        //TextView for debugging purposes
        TextView debugView = (TextView) findViewById(R.id.debug);

        //buttons to go to activities
        day = (Button) findViewById(R.id.day);
        month = (Button) findViewById(R.id.month);
        info = (Button) findViewById(R.id.info);
        options = (Button) findViewById(R.id.options);
        disclaimer = (Button) findViewById(R.id.disclaimer);

        //get information from info activity
        Intent getInfo = getIntent();

        //get gender and weight
        String gender = getInfo.getStringExtra(Information.GENDER);
        int weight = getInfo.getIntExtra(Information.WEIGHT, 0);



        day.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                openDay();
            }
        });

        month.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                openMonth();
            }
        });

        info.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                openInfo();
            }
        });

        options.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                openOptions();
            }
        });

        disclaimer.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                openDisclaimer();
            }
        });
    }

    public void openDay()
    {
        Intent intent = new Intent(this, DayTracker.class);
        startActivity(intent);
    }

    public void openMonth()
    {
        Intent intent = new Intent(this, MonthTracker.class);
        startActivity(intent);
    }

    public void openInfo()
    {
        Intent intent = new Intent(this, Information.class);
        startActivity(intent);
    }

    public void openOptions()
    {
        Intent intent = new Intent(this, Options.class);
        startActivity(intent);
    }

    public void openDisclaimer()
    {
        Intent intent = new Intent(this, Disclaimer.class);
        startActivity(intent);
    }
}