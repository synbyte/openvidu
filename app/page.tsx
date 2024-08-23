import Image from "next/image";
import Link from "next/link";

export default function Home() {
  return (
    <main className="flex flex-col justify-between items-center p-24 min-h-screen">
      <div className='flex flex-col justify-center items-center p-10 rounded-xl shadow-md shadow-black bg-slate-800'>
        <p>Video platform test.</p>
        <Link href='/room'><button className='p-3 my-5 rounded-lg shadow-lg transition-all duration-200 bg-slate-500 hover:shadow-sm shadow-black hover:shadow-cyan-300'>Enter Room</button></Link>
        <p className='text-xs tracking-wide uppercase text-shadow'>Make sure to allow access to mic and cam.</p>

        </div>

     
    </main>
  );
}
