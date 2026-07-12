# $NetBSD$

DISTNAME=	ml_dtypes-0.5.4
PKGNAME=	${PYPKGPREFIX}-${DISTNAME:S/_/-/}
CATEGORIES=	devel math
MASTER_SITES=	${MASTER_SITE_PYPI:=m/ml_dtypes/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/ml_dtypes/
COMMENT=	several NumPy dtype extensions used in machine learning
LICENSE=	apache-2.0

USE_LANGUAGES+=	c++

DEPENDS+=	${PYPKGPREFIX}-numpy>=2.3.0:../../math/py-numpy

# url2pkg-marker (please do not remove this line.)
.include "../../math/py-numpy/buildlink3.mk"
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
