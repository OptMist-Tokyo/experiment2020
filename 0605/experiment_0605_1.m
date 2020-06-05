global NumOfStudents NumOfSeats numDim;

%name = {'Seats 1','Seats 1','Seats 1','Office 4','Office 5','Office 6','Office 7'};
%printofficeassign(name)

NumOfStudents = size(cdf06051,1);
NumOfSeats = size(cdf06051,2);
numDim = NumOfStudents * NumOfSeats;

onesvector = ones(1,NumOfSeats);

c_data_NM = cdf06051(:);

Aeq = zeros(NumOfStudents,numDim);
beq = ones(NumOfStudents,1);

for i = 1:NumOfStudents
    Aeq(i, (i-1)*NumOfSeats+1 : i*NumOfSeats) = ones(1,NumOfSeats);
end

A = repmat(eye(NumOfSeats),1,NumOfStudents);
b = ones(NumOfSeats,1);

f = -c_data_NM;
lb = zeros(size(f));
ub = lb + 1;
intvars = 1:length(f);
[x,fval,exitflag,output] = intlinprog(f,intvars,A,b,Aeq,beq,lb,ub);

x_mat = reshape(x,[NumOfSeats,NumOfStudents]);
x_seats = zeros(NumOfSeats,1);

for j = 1:NumOfSeats
    for i = 1:NumOfStudents
        if x_mat(j,i)==1
           x_seats(j,1) = i;
        end
    end
end
x_seats_binary = x_seats > 0;
x_seats_binary = reshape(x_seats_binary,5,10);

utility_vec = zeros(NumOfStudents,1);
for i = 1:NumOfStudents
    utility_vec(i) = dot(cdf06051(i,:),x_mat(:,i));
end