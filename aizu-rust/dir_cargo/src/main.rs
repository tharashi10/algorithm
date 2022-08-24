fn main(){
    let mut s: String = String::new();
    let result: std::io::Result<usize> = std::io::stdin().read_line(&mut s);
    match result {
        Ok(_) => {
            println!("{}",s);
        }
        Err(err) => {
            println!("{}",err);
        }
    }
}
