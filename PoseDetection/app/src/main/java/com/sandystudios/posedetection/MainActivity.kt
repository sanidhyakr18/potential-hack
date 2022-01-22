package com.sandystudios.posedetection

import android.content.ContentValues.TAG
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.view.MotionEvent
import android.view.View
import android.widget.ImageView
import android.widget.LinearLayout
import androidx.core.content.ContextCompat
import androidx.viewpager.widget.ViewPager
import androidx.viewpager.widget.ViewPager.OnPageChangeListener
import com.sandystudios.posedetection.adapter.CustomPagerAdapter

class MainActivity : AppCompatActivity() {

    private var mResources = intArrayOf(R.drawable.boxing, R.drawable.kohli, R.drawable.badminton)

    private lateinit var mViewPager: ViewPager
    private var mAdapter: CustomPagerAdapter? = null
    private var pagerIndicator: LinearLayout? = null
    private var dotsCount = 0
    private lateinit var dots: MutableList<ImageView>

//    // creating object of ViewPager
//    private var mViewPager: ViewPager? = null
//
//    // images array
//    private var images = intArrayOf(R.drawable.boxing, R.drawable.kohli, R.drawable.badminton)
//
//    // Creating Object of ViewPagerAdapter
//    private var mViewPagerAdapter: ViewPagerAdapter? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

//        // Initializing the ViewPager Object
//        mViewPager = findViewById<View>(R.id.viewPagerMain) as ViewPager
//
//        // Initializing the ViewPagerAdapter
//        mViewPagerAdapter = ViewPagerAdapter(this@MainActivity, images)
//
//        // Adding the Adapter to the ViewPager
//        mViewPager!!.adapter = mViewPagerAdapter

        mViewPager = findViewById(R.id.viewpager)
        pagerIndicator = findViewById<View>(R.id.viewPagerCountDots) as LinearLayout
        mAdapter = CustomPagerAdapter(this, mResources)
        mViewPager.adapter = mAdapter
        mViewPager.currentItem = 0
        mViewPager.addOnPageChangeListener(object : OnPageChangeListener {
            override fun onPageScrolled(
                position: Int,
                positionOffset: Float,
                positionOffsetPixels: Int
            ) {
            }

            override fun onPageSelected(position: Int) {
                for (i in 0 until dotsCount) {
                    dots[i].setImageDrawable(
                        ContextCompat.getDrawable(
                            applicationContext,
                            R.drawable.nonselecteditem_dot
                        )
                    )
                }
                dots[position].setImageDrawable(
                    ContextCompat.getDrawable(
                        applicationContext,
                        R.drawable.selecteditem_dot
                    )
                )
            }

            override fun onPageScrollStateChanged(state: Int) {}
        })

        setPageViewIndicator()
    }

    private fun setPageViewIndicator() {
        dotsCount = mAdapter!!.count
        dots = ArrayList()
        for (i in 0 until dotsCount) {
            Log.e(TAG, "setPageViewIndicator: $i")
            dots[i] = ImageView(this)
            dots[i].setImageDrawable(
                ContextCompat.getDrawable(
                    applicationContext,
                    R.drawable.nonselecteditem_dot
                )
            )
            val params = LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.WRAP_CONTENT,
                LinearLayout.LayoutParams.WRAP_CONTENT
            )
            params.setMargins(6, 0, 6, 0)
            dots[i].setOnTouchListener(View.OnTouchListener { v, event ->
                mViewPager!!.currentItem = i
                true
            })
            pagerIndicator?.addView(dots[i], params)
        }
        dots[0].setImageDrawable(
            ContextCompat.getDrawable(
                applicationContext,
                R.drawable.selecteditem_dot
            )
        )
    }
}