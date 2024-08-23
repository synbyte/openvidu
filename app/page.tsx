import Image from "next/image";
import Link from "next/link";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className='flex flex-col p-10 rounded-xl shadow-md shadow-black bg-slate-800 items-center justify-center'>
        <p>Video platform test.</p>
        <Link href='/room'><button className='my-5 bg-slate-500 p-3 rounded-lg ring-2 ring-cyan-800 shadow-md shadow-black hover:shadow-cyan-300 transition-all duration-200'>Enter Room</button></Link>
        <p className='text-xs text-shadow uppercase tracking-wide'>Make sure to allow access to mic and cam.</p>

        </div>

     
    </main>
  );
}
