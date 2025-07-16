export function Header({title}) {
  return (
   <div>
    <h1>{title}</h1>
   </div>
  );
}

export function Header1(props){
    return (
     <div>
        <h1>{props.titles}</h1>
     </div>
    );
}

export default Header1;