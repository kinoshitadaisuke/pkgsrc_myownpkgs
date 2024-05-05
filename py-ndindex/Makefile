# $NetBSD$

DISTNAME=	ndindex-1.8
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	math
MASTER_SITES=	${MASTER_SITE_PYPI:=n/ndindex/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/ndindex/
COMMENT=	Python library for manipulating indices of ndarrays
LICENSE=	mit

DEPENDS+=	${PYPKGPREFIX}-numpy>=0:../../math/py-numpy

# url2pkg-marker (please do not remove this line.)
.include "../../lang/python/wheel.mk"
.include "../../math/py-numpy/buildlink3.mk"
.include "../../mk/bsd.pkg.mk"
